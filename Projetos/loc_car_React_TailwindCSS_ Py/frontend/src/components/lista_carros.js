import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
	const [carros, setCarros] = useState([]);
	const [loading, setLoading] = useState(true);

	useEffect(() => {
		// Aqui você pode pegar os carros da sua API backend, ou usar os dados hardcoded
		axios
			.get("/api/carros")
			.then((response) => {
				setCarros(response.data.carros); // Atualizando o estado com a lista de carros
				setLoading(false); // Desativando o estado de carregamento
			})
			.catch((error) => {
				console.error("Erro ao buscar carros:", error);
				setLoading(false);
			});
	}, []);

	if (loading) {
		return <div>Carregando...</div>;
	}

	return (
		<div className="container mx-auto p-4">
			<h1 className="text-2xl font-bold mb-4">Locadora de Carros 🚗</h1>
			<h2 className="text-xl mb-4">Carros Disponíveis</h2>
			<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
				{carros.map((carro) => (
					<div key={carro.id} className="border p-4 rounded shadow-md">
						<h3 className="text-xl font-semibold">{carro.nome}</h3>
						<p className="text-lg">Preço por dia: R$ {carro.preco}</p>
						{/* biome-ignore lint/a11y/useButtonType: <explanation> */}
						<button className="mt-4 bg-blue-500 text-white px-4 py-2 rounded">
							Alugar
						</button>
					</div>
				))}
			</div>
		</div>
	);
}

export default App;
