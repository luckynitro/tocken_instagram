// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PublicidadContract {
    address public owner;
    mapping(address => uint256) public pagos;

    event AnuncioPublicado(address anunciante, uint256 costo);

    constructor() {
        owner = msg.sender;
    }

    modifier soloPropietario() {
        require(msg.sender == owner, "Solo el propietario puede realizar esta operación");
        _;
    }

    function publicarAnuncio(uint256 costo) external payable {
        require(msg.value >= costo, "No se ha proporcionado el monto de pago requerido");
        pagos[msg.sender] += msg.value;
        emit AnuncioPublicado(msg.sender, msg.value);
    }

    function retirarFondos() external soloPropietario {
        payable(owner).transfer(address(this).balance);
    }
}
