const fs = require('fs').promises;

async function countStudents(path) {
    try {
        const data = await fs.readFile(path, 'utf8');
        const lines = data.split('\n').filter(line =>
line.trim() !== '');
        const students = lines.slice(1);
        
        console.log(`Number of students: ${students.length}`);
        let output = `Number of students: ${students.length}\n`;

        const fields = {};
        for (const student of students) {
            const [firstName, , , field] = student.split(',');
            if (!fields[field]) {
                fields[field] = [];
            }
            fields[field].push(firstName);
        }

        for (const [field, students] of Object.entries(fields))
    {
        console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
        output += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
    }

        return output.trim();
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;