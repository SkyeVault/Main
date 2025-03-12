import * as Client from '@web3-storage/w3up-client'
import { filesFromPaths } from 'files-from-path'

const client = await Client.create()

// first time setup!
if (!Object.keys(client.accounts()).length) {
  // waits for you to click the link in your email to verify your identity
  const account = await client.login('you@example.org')
  // create a space for your uploads
  const space = await client.createSpace('lets-go')
  // save the space to the store, and set as "current"
  await space.save()
  // associate this space with your account
  await account.provision(space.did())
}

// content-address your files
const files = await filesFromPaths(['./best-gifs'])
const root = await client.uploadDirectory(files)

console.log(root.toString()) // bafy...
