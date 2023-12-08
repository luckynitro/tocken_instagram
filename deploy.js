// deploy.js o cualquier otro script
const { ethers } = require("hardhat");

async function main() {
  const PublicidadContract = await ethers.getContractFactory("PublicidadContract");
  const publicidadContract = await PublicidadContract.deploy();

  await publicidadContract.deployed();

  console.log("Contrato desplegado en:", publicidadContract.address);

  // Publica un anuncio con un costo de 1 ether (ajusta según sea necesario)
  const costoAnuncio = ethers.utils.parseEther("1");
  const publicarAnuncioTx = await publicidadContract.publicarAnuncio(costoAnuncio);
  await publicarAnuncioTx.wait();

  console.log("Anuncio publicado");
}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });

