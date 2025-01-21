const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
    const { url } = req;
  
  if (url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    res.writeHead(200, {'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');

    const databasePath = process.argv[2];
    countStudents(databasePath)
        .then((data) => {
          res.end(data);
        })
        .catch((error) => {
            res.end(error.message);
        });
  } else {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server running on port 1245');
});

module.exports = app;