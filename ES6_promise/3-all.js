import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      const [photo, user] = results;
      console.log(photo.body);
      console.log(user.firstName, user.lastName);
    }).catch(() => {
      console.log('Signup system offline');
    });
}
