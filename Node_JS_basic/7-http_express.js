const express = require('express');
const fs = require('fs');
const path = require('path');
const countStudents = require('./3-read_file_async');

// Crée une instance d'application Express
const app = express();

// Endpoint pour la racine "/"
app.get('/', (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
    const databaseFile = process.argv[2]; // Le fichier CSV passé en argument
  
    if (!databaseFile) {
      res.status(500).send('This is the list of our students\nCannot load the database');
      return;
    }
  
    countStudents(databaseFile)
      .then((data) => {
        res.send(`This is the list of our students\n${data}`);
      })
      .catch(() => {
        res.status(500).send('This is the list of our students\nCannot load the database');
      });
});

// Le serveur écoute sur le port 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

module.exports = app;