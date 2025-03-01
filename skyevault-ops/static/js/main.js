document.addEventListener('DOMContentLoaded', function () {
    function fetchLogs() {
        fetch('/logs')
            .then(response => response.json())
            .then(data => {
                let logOutput = document.getElementById('log-output');
                logOutput.innerHTML = "";
                data.forEach(log => {
                    logOutput.innerHTML += `[${log.service}] ${log.status} - ${log.message}\\n`;
                });
            })
            .catch(error => console.error('Error fetching logs:', error));
    }

    setInterval(fetchLogs, 5000); // Refresh logs every 5 seconds
    fetchLogs(); // Initial load
});
