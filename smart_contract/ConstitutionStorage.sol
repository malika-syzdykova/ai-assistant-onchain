// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ConstitutionStorage {
    struct Vector {
        string contentId;
        string data;
    }

    mapping(string => string) public vectors;

    function storeVector(string memory contentId, string memory data) public {
        vectors[contentId] = data;
    }

    function getVector(string memory contentId) public view returns (string memory) {
        return vectors[contentId];
    }
}
