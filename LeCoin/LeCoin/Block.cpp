#include <iostream>


using namespace std;


class Block {


public:
	
	string transactionHash;
	string prevHash;
	string incompleteHash;
	string hash;
	int ProofOfWork;


	Block(string prevHash /*Include Transaction Object here*/) {

		Block::prevHash = prevHash;


	}

	string calculateIncompleteHash(string transactionHash,string prevHash ) {

		
	
	}


	string calculateHash(string transactionHash, string prevHash) {

		

	}





};

