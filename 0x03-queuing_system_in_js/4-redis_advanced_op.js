import { createClient, print } from "redis";

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected tot he server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});

const updateHash = (hashName, fieldName, filedValue) => {
  client.HSET(hashName, fieldName, filedValue, print);
};

const printHash = (hashName) => {
  client.HGETALL(hashName, (_err, reply) => console.log(reply));
};

const main = () =>  {
  const obj = {Portland: 50, Seatle: 80, 'New York': 20, Bogota: 20, Cali: 40, Paris: 2};

  for (const [field, value] of Object.entries(obj)) {
    updateHash('HolbertonSchools', field, value);
  }
  printHash('HolbertonSchools');
};
