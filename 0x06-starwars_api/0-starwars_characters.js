#!/usr/bin/node
//a script that prints all characters of a Star Wars movie

const request = require('request');

async function processRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, function(error, response, body) {
        if (error) {
          reject(error)
        }
        resolve({response, body})
    })
  })
}

async function main() {
  if (process.argv.length > 2) {
    const id = process.argv[2]
    try {
        const {_, body} =  await processRequest(
          `https://swapi-api.alx-tools.com/api/films/${id}`
        )
    
        const characters = JSON.parse(body).characters
        if (characters.length > 0) {
          const downloadPromises = characters.map(async (url) => {
            const {_, body} = await processRequest(url)
            return JSON.parse(body).name
          })
          const result = await Promise.all(downloadPromises)
          console.log(result.join('\n'))
        }
      } catch(error) {
        console.log(error)
      }
  }
}
main()
.then(() => null)
.catch((error) => console.log('script failed', error))
