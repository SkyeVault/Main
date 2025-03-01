document.addEventListener('DOMContentLoaded', function () {
    function fetchLogs() {
        fetch('/logs')
            .then(response => response.json())
            .then(data => {
                let logOutput = document.getElementById('log-output');
                logOutput.innerHTML = "";
                data.forEach(log => {
                    logOutput.innerHTML += `[${log.script}] ${log.output}\n`;
                });
            })
            .catch(error => console.error('Error fetching logs:', error));
    }

    setInterval(fetchLogs, 10000);  // Refresh every 10 seconds
    fetchLogs();

    // Button to manually run security scripts
    document.getElementById("run-blue-team").addEventListener("click", function () {
        fetch('/run-blue-team')
            .then(response => response.json())
            .then(data => alert(data.status))
            .catch(error => console.error('Error running Blue Team scripts:', error));
    });
});

