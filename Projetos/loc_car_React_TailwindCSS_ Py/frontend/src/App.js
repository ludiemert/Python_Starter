import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
	const [carros, setCarros] = useState([]);
	const [dias, setDias] = useState(1);

	// Requisição para pegar os carros da API
	useEffect(() => {
		axios
			.get("http://127.0.0.1:5000/api/carros")
			.then((response) => setCarros(response.data.carros))
			.catch((error) => console.error(error));
	}, []);

	// Função para alugar o carro
	const alugarCarro = (id) => {
		axios
			.post("http://127.0.0.1:5000/api/alugar", { id, dias })
			.then((response) => {
				alert(response.data.message);
				window.location.reload(); // Atualiza a página
			})
			.catch((error) => console.error(error));
	};

	// Função para devolver o carro
	const devolverCarro = (id) => {
		axios
			.post("http://127.0.0.1:5000/api/devolver", { id })
			.then((response) => {
				alert(response.data.message);
				window.location.reload(); // Atualiza a página
			})
			.catch((error) => console.error(error));
	};

	return (
		<div className="p-5">
			<h1 className="text-3xl font-bold text-center mb-5">
				Locadora de Carros 🚗
			</h1>
			<h2 className="text-2xl font-semibold">Carros Disponíveis:</h2>

			<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 mt-5">
				{carros.map((carro) => (
					<div key={carro.id} className="p-4 border rounded shadow">
						<h3 className="text-lg font-bold">{carro.nome}</h3>
						<p>R$ {carro.preco} / dia</p>
						<input
							type="number"
							className="border p-1 mt-2"
							value={dias}
							onChange={(e) => setDias(e.target.value)} // Atualiza os dias de aluguel
						/>
						{/* biome-ignore lint/a11y/useButtonType: <explanation> */}
						<button
							onClick={() => alugarCarro(carro.id)} // Chama a função para alugar o carro
							className="bg-blue-500 text-white px-3 py-1 rounded mt-2"
						>
							Alugar
						</button>
						{/* biome-ignore lint/a11y/useButtonType: <explanation> */}
						<button
							onClick={() => devolverCarro(carro.id)} // Chama a função para devolver o carro
							className="bg-red-500 text-white px-3 py-1 rounded mt-2"
						>
							Devolver
						</button>
					</div>
				))}
			</div>
		</div>
	);
}

export default App;
