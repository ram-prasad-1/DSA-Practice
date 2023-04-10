async function logJSONData() {
  const response = await fetch('http://example.com/movies.json');
  if (response.ok) {
    const jsonData = await response.json();
    console.log(jsonData);
  }
}

async function postJSON(data) {
  try {
    const response = await fetch('https://example.com/profile', {
      method: 'POST', // or 'PUT'
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    const result = await response.json();
    console.log(result);
  } catch (error) {
    console.log(error);
  }
}
