# Task1Blockchain

1 a>Q> Define blockchain in your own words (100–150 words).
 
1 a>Ans> Blockchain is a decentralized chain of blocks which stores data and can perform transactions with each other. Each block contains a Blockheader and the List of all transactions . The block header contains nonce, merkle tree, previous hash,data and time stamp. BlockChain is maintained by distributed network of nodes which agree to do so because of consensus algorithms like proof of work, proof of stake.etc . What makes blockchain secure and trustless is that it is maintained by a distributed network of nodesThis distributed consensus makes blockchain tamper-resistant,transparent, and ideal for use cases where data immutability and trust are essential.


1 b>Q>List 2 real-life use cases (e.g., supply chain, digital identity).
1 b>Ans> supply chain management :Tracks goods transparently from origin to consumer, ensuring authenticity (e.g., IBM Food Trust).
digital Identity: Provides tamper-proof, self-sovereign identity verification (e.g., Estonia’s e-Residency program).

2 a>Draw a block showing: data, previous hash, timestamp, nonce, and Merkle root.
2 a>Ans> 

|           Block structure            |
|--------------------------------------|
| Index: 1                             |
| Timestamp: 2025-06-09 21:00:00       |
| Data: {"amount": 50, "sender": "A"}  |
| Previous Hash: a8f5...               |
| Nonce: 2342                          |
| Merkle Root: b3c1...                 |
+--------------------------------------+
2>b>Q>Briefly explain with an example how the Merkle root helps verify data integrity.
2>b>Ans> Merkle root is a value obtained which contains all the data of transactions of a block which is obtained by repeatedly hashing of transactions, until a sigle root value is generated. For ex: If two transactions (T1, T2) have hashes h1, h2, then the Merkle root is H(h1 + h2). If T2 changes, the root changes—making tampering detectable quickly.

3>Q>Explain in brief (4–5 sentences each):

a>What is Proof of Work and why does it require energy?

b>What is Proof of Stake and how does it differ?

c>What is Delegated Proof of Stake and how are validators selected?



3>Ans>
a>Proof of Work (PoW): PoW requires participants (miners) to solve computational puzzles to validate blocks. This consumes energy due to repeated hashing and trial/error, securing the network against spam and fraud.

b>Proof of Stake (PoS): PoS selects validators based on the amount of cryptocurrency they “stake.” More stake = higher chance to validate. It saves energy by removing the need for heavy computation.

c> Delegated Proof of Stake (DPoS): Token holders vote to elect a few trusted delegates to validate transactions. Validators are chosen based on popularity rather than wealth or computation, enabling faster consensus.



