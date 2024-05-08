import { createClient, print } from "redis";
import {promisify} from 'util';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect',  async () => {
  console.log('Redis client connected to the serve');
  await main();
});

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
}

const displaySchoolValue = async (schoolName) => {
  const name = await promisify(client.GET).bind(client)(schoolName);
  console.log(name);
};

const main = async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}
