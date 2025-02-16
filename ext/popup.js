// popup.js

document.addEventListener('DOMContentLoaded', () => {
    const agentIdDiv = document.getElementById('agent-id');
  
    chrome.storage.local.get('agent_id', (res) => {
      if (res.agent_id) {
        agentIdDiv.textContent = res.agent_id;
      } else {
        agentIdDiv.textContent = 'No agent_id found. Registration pending.';
      }
    });
  });
  