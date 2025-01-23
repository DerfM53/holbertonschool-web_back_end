const express = require('express');

// Crée une instance d'application Express
const app = express();

// Endpoint pour la racine "/"
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Le serveur écoute sur le port 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

module.exports = app;