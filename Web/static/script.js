(function() {
    const container = document.getElementById('logContainer');
    const cmdInput = document.getElementById('cmdInput');
    const sendBtn = document.getElementById('sendBtn');
    const logCountEl = document.getElementById('logCount');
    let lastLogCount = 0;

    function escapeHtml(text) {
        if (typeof text !== 'string') text = String(text);
        const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
        return text.replace(/[&<>"']/g, function(m) { return map[m]; });
    }

    function safeString(value) {
        if (value === null || value === undefined) return '';
        if (typeof value === 'string') return value;
        try {
            return JSON.stringify(value);
        } catch {
            return String(value);
        }
    }

    function toggleContent(id) {
        const preview = document.getElementById(id + '_preview');
        const full = document.getElementById(id + '_full');
        const btn = document.getElementById(id + '_btn');
        if (full.style.display === 'none') {
            full.style.display = 'inline';
            preview.style.display = 'none';
            btn.textContent = '[收起]';
        } else {
            full.style.display = 'none';
            preview.style.display = 'inline';
            btn.textContent = '[展开]';
        }
    }

    function createEntryHtml(log) {
        const role = log.role || 'system';
        const rawContent = safeString(log.content);
        const roleClass = role.replace(/[^a-zA-Z]/g, '');
        const fullContent = escapeHtml(rawContent);
        const isLong = rawContent.length > 300;
        const enableExpand = (role === 'TOOL' && isLong);

        if (enableExpand) {
            const previewText = escapeHtml(rawContent.slice(0, 300));
            const id = 'msg_' + Math.random().toString(36).substr(2, 8);
            return `<div class="entry">
                        <span class="role-tag ${roleClass}">${role}</span>
                        <span class="msg">
                            <span id="${id}_preview">${previewText}...</span>
                            <span id="${id}_full" style="display:none;">${fullContent}</span>
                            <span class="expand-btn" id="${id}_btn" onclick="toggleContent('${id}')">[展开]</span>
                        </span>
                    </div>`;
        } else {
            return `<div class="entry">
                        <span class="role-tag ${roleClass}">${role}</span>
                        <span class="msg">${fullContent || '<span class="empty-hint">（空）</span>'}</span>
                    </div>`;
        }
    }

    function fullRender(logs) {
        if (!logs || logs.length === 0) {
            container.innerHTML = `<div class="empty-state"><div class="icon">🜁</div><div>等待指令</div></div>`;
            return;
        }
        let html = '';
        for (const log of logs) {
            html += createEntryHtml(log);
        }
        container.innerHTML = html;
    }

    function fetchLogs() {
        fetch('/logs')
            .then(r => r.json())
            .then(data => {
                const logs = data.logs || [];
                const total = logs.length;
                logCountEl.textContent = total;

                const atBottom = container.scrollHeight - container.scrollTop - container.clientHeight < 20;

                if (total === 0) {
                    if (lastLogCount !== 0) {
                        fullRender(logs);
                        lastLogCount = 0;
                    }
                    return;
                }

                if (lastLogCount === 0 || total < lastLogCount) {
                    fullRender(logs);
                    lastLogCount = total;
                    if (atBottom) {
                        container.scrollTop = container.scrollHeight;
                    }
                    return;
                }

                if (total > lastLogCount) {
                    const newLogs = logs.slice(lastLogCount);
                    let html = '';
                    for (const log of newLogs) {
                        html += createEntryHtml(log);
                    }
                    container.insertAdjacentHTML('beforeend', html);
                    lastLogCount = total;
                    if (atBottom) {
                        container.scrollTop = container.scrollHeight;
                    }
                }
            })
            .catch(() => {});
    }

    function sendCommand() {
        const cmd = cmdInput.value.trim();
        if (!cmd) return;
        fetch('/command', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ command: cmd })
        }).then(() => {
            cmdInput.value = '';
            fetchLogs();
        });
    }

    cmdInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') { e.preventDefault(); sendCommand(); }
    });
    sendBtn.addEventListener('click', sendCommand);

    window.toggleContent = toggleContent;

    fetchLogs();
    setInterval(fetchLogs, 3000);
})();