fetch('test_data.json')
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById('data-container');
    data.forEach(entry => {
      const div = document.createElement('div');
      div.textContent = `${entry.name}: ${entry.score}`;
      container.appendChild(div);
    });
  });
