export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const success = true;
      if (success) {
        resolve("Réponse de l'API");
      } else {
        reject(new Error("Erreur lors de l'appel à l'API"));
      }
    }, 1000);
  });
}
