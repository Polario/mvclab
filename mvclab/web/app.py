from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import subprocess

app = FastAPI(title="mvclab Web UI")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return """
    <html>
        <head>
            <title>mvclab Framework</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
            <style>
                body { font-family: 'Roboto', Arial, sans-serif; background: #f7f9fa; margin: 0; padding: 0; }
                header { background: #22223b; color: #fff; padding: 24px 0 16px 0; text-align: center; box-shadow: 0 2px 8px #0001; }
                h1 { margin: 0; font-size: 2.5rem; letter-spacing: 2px; }
                nav { margin-top: 12px; }
                nav button { background: #4a4e69; color: #fff; border: none; padding: 10px 24px; margin: 0 4px; border-radius: 4px; font-size: 1rem; cursor: pointer; transition: background 0.2s; }
                nav button.active, nav button:hover { background: #9a8c98; }
                main { max-width: 700px; margin: 32px auto; background: #fff; border-radius: 8px; box-shadow: 0 2px 16px #0002; padding: 32px; }
                .tabcontent { display: none; }
                .tabcontent.active { display: block; }
                .test-btn { background: #22223b; color: #fff; border: none; padding: 10px 20px; border-radius: 4px; font-size: 1rem; cursor: pointer; margin-bottom: 16px; }
                .test-btn:hover { background: #4a4e69; }
                pre { background: #f0f0f0; padding: 16px; border-radius: 4px; overflow-x: auto; }
                .footer { text-align: center; color: #888; margin-top: 40px; font-size: 0.95rem; }
                a { color: #4a4e69; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <header>
                <h1>mvclab Framework</h1>
                <div>Modular Git Automation with Intelligent Agents</div>
                <nav>
                    <button onclick="openTab(event, 'Home')" class="active">Home</button>
                    <button onclick="openTab(event, 'Test')">Test</button>
                    <button onclick="openTab(event, 'About')">About</button>
                </nav>
            </header>
            <main>
                <div id="Home" class="tabcontent active">
                    <h2>Welcome to mvclab</h2>
                    <p><b>mvclab</b> is a robust, agent-based framework for managing Git-based projects. Use the navigation above to explore features or run tests.</p>
                    <ul>
                        <li>Automated branch, commit, merge, and review agents</li>
                        <li>Release and tagging automation</li>
                        <li>Conflict detection and resolution</li>
                        <li>History and contributor analysis</li>
                        <li>Configurable agents and project templates</li>
                        <li>CLI and Web UI for all operations</li>
                    </ul>
                    <p>See the <a href="https://github.com/your-org/mvclab" target="_blank">project repository</a> for documentation and source code.</p>
                </div>
                <div id="Test" class="tabcontent">
                    <h2>Run All Tests</h2>
                    <button class="test-btn" onclick="runTests()">Run All Tests</button>
                    <pre id="testOutput">Click the button to run all mvclab agent tests.</pre>
                </div>
                <div id="About" class="tabcontent">
                    <h2>About mvclab</h2>
                    <p>mvclab is designed to enforce best practices, automate repetitive Git tasks, and provide a consistent workflow for teams and individuals. All operations are performed through intelligent agents, ensuring auditability and reliability.</p>
                    <p>For more information, see the <a href="/docs" target="_blank">API documentation</a> or <a href="https://github.com/your-org/mvclab" target="_blank">GitHub repository</a>.</p>
                </div>
            </main>
            <div class="footer">
                &copy; 2024 mvclab &mdash; Modular Git Automation Framework
            </div>
            <script>
                function openTab(evt, tabName) {
                    var i, tabcontent, tablinks;
                    tabcontent = document.getElementsByClassName("tabcontent");
                    for (i = 0; i < tabcontent.length; i++) {
                        tabcontent[i].classList.remove("active");
                    }
                    tablinks = document.querySelectorAll("nav button");
                    for (i = 0; i < tablinks.length; i++) {
                        tablinks[i].classList.remove("active");
                    }
                    document.getElementById(tabName).classList.add("active");
                    evt.currentTarget.classList.add("active");
                }
                function runTests() {
                    document.getElementById('testOutput').innerText = 'Running tests...';
                    fetch('/run_tests')
                        .then(response => response.text())
                        .then(data => {
                            document.getElementById('testOutput').innerText = data;
                        });
                }
            </script>
        </body>
    </html>
    """

@app.get("/run_tests", response_class=HTMLResponse)
async def run_tests():
    try:
        result = subprocess.run(["python", "test_git_agents.py"], capture_output=True, text=True)
        return f"<pre>{result.stdout + result.stderr}</pre>"
    except Exception as e:
        return f"<pre>Error running tests: {str(e)}</pre>" 