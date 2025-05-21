// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract KnowledgeBase {
    struct QA {
        string question;
        string answer;
    }

    QA[] public knowledge;

    function addQA(string memory question, string memory answer) public {
        knowledge.push(QA(question, answer));
    }

    function getQA(uint index) public view returns (string memory, string memory) {
        require(index < knowledge.length, "Out of bounds");
        return (knowledge[index].question, knowledge[index].answer);
    }

    function getCount() public view returns (uint) {
        return knowledge.length;
    }
}
