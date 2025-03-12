# Connecting the Web of Data with Web3.Storage

## Overview

Eliminate silos with **Web3.Storage**. Using **IPFS** and other decentralized protocols, you can create a true data layer that connects you, your users, and the Web, regardless of where content is stored—client-side, in the cloud, or elsewhere.

This guide provides step-by-step instructions to get started with **Web3.Storage**, covering authentication, creating a storage space, and uploading files.

## Why Web3.Storage?

- **Decentralized and Redundant:** Uses IPFS to ensure content is available and verifiable.
- **Easy-to-Use Client Libraries:** Abstracts the complexity of decentralized protocols.
- **Best-in-Class Performance:** Competitive with Web2 storage solutions.
- **No Vendor Lock-in:** Store content anywhere and access it seamlessly.

## Prerequisites

Before you begin, ensure you have:

- **Node.js** (Recommended: latest LTS version)
- **NPM or Yarn** installed
- A **Web3.Storage** account

## Installation

To use Web3.Storage in your project, install the `@web3-storage/w3up-client` package.

```sh
npm install @web3-storage/w3up-client files-from-path
```

## Setting Up Web3.Storage

This section guides you through the first-time setup, including authentication and creating a storage space.

### 1. Import Dependencies

```js
import * as Client from '@web3-storage/w3up-client'
import { filesFromPaths } from 'files-from-path'
```

### 2. Create a Client Instance

```js
const client = await Client.create()
```

### 3. Authenticate and Create a Storage Space

If this is your first time using Web3.Storage, follow these steps:

1. **Authenticate with your email.** The system will send a verification link.
2. **Create a storage space.** This acts as a namespace for your uploads.
3. **Associate the space with your account.** This allows you to manage stored files.

```js
// First-time setup
if (!Object.keys(client.accounts()).length) {
  const account = await client.login('you@example.org') // Verify via email
  const space = await client.createSpace('lets-go') // Create a storage space
  await space.save() // Save the space to your local store
  await account.provision(space.did()) // Associate space with your account
}
```

## Uploading Files to Web3.Storage

After setting up your account, you can **content-address** your files and upload them.

### 1. Select Files from a Directory

Use the `files-from-path` package to select files from a local directory.

```js
const files = await filesFromPaths(['./best-gifs'])
```

### 2. Upload Files to IPFS

Use the `uploadDirectory` method to store the files on **Web3.Storage**.

```js
const root = await client.uploadDirectory(files)
```

### 3. Retrieve the IPFS CID

Once uploaded, Web3.Storage provides a **Content Identifier (CID)**, which you can use to retrieve the files.

```js
console.log(root.toString()) // Example output: bafy...
```

## Accessing Files

After uploading, use any IPFS gateway to access the stored content.

```sh
https://dweb.link/ipfs/<CID>
```

Replace `<CID>` with the actual identifier returned in the previous step.

## Conclusion

With **Web3.Storage**, you can take full advantage of **IPFS-based storage** without worrying about infrastructure complexity. Whether you are building decentralized applications, archiving content, or integrating blockchain technology, this approach ensures data persistence and availability.

For more details, visit the [Web3.Storage Documentation](https://web3.storage/docs/).

