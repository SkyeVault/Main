document.addEventListener('DOMContentLoaded', function () {
    function fetchLogs() {
        fetch('/logs')
            .then(response => response.json())
            .then(data => {
                let logOutput = document.getElementById('log-output');
                logOutput.innerHTML = "";
                data.forEach(log => {
                    logOutput.innerHTML += `[${log.service}] ${log.status} - ${log.message}\n`;
                });
            })
            .catch(error => console.error('Error fetching logs:', error));
    }

    setInterval(fetchLogs, 5000);
    fetchLogs();

    // Chart.js Placeholder for Security Insights Graph
    const ctx = document.getElementById('securityGraph').getContext('2d');
    const securityChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['IAM', 'CloudTrail', 'GuardDuty', 'WAF'],
            datasets: [{
                label: 'Threat Level',
                data: [3, 1, 5, 2],  // Simulated Data
                backgroundColor: ['red', 'yellow', 'purple', 'blue']
            }]
        },
        options: {
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    // Red Team Buttons
    window.launchScan = function () {
        alert("🚀 Running Network Scan...");
    };

    window.privilegeEscalation = function () {
        alert("⚠️ Attempting Privilege Escalation...");
    };

    window.runExploit = function () {
        alert("💥 Exploiting S3 Bucket...");
    };
});
