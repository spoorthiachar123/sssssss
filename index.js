const express = require("express");
const app = express();

app.use(express.json());
app.post("/answer", async (req, res) => {

  const options = {
    method: 'POST',
    url: 'https://openai80.p.rapidapi.com/models?q=about nature',
    headers: {
      'content-type': 'application/json',
      'X-RapidAPI-Key': '452767ea12mshb74b97343375335p128f0ajsn4d2ca9abd7c8',
      'X-RapidAPI-Host': 'openai80.p.rapidapi.com'
    },
    body: `{"model":"gpt-3.5-turbo","messages":[{"role":"user","content":"how to eat"}]}`
  };

  fetch(
    'https://openai80.p.rapidapi.com/chat/completions',
    options
  ).then((response) => response.json())
    .then((response) => {
      console.log(response.choices[0].message.content)
    })
})