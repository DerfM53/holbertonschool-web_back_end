// 1-promise.js
export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (success === true) { // Vérifiez si success est vrai
        resolve({
          status: 200,
          body: 'Success', // Assurez-vous que l'orthographe est correcte
        });
      } else {
        reject(new Error('The fake API is not working currently')); // Rejetez avec un objet Error
      }
    }, 1000); // Délai de 1 seconde pour simuler une opération asynchrone
  });
}
