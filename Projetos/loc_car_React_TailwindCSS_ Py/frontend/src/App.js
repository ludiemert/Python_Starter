import { useState, useEffect } from "react";
import axios from "axios";

const App = () => {
	const [carrosDisponiveis, setCarrosDisponiveis] = useState([]);
	const [carrosAlugados, setCarrosAlugados] = useState([]);

	useEffect(() => {
		const fetchData = async () => {
			const { data } = await axios.get("http://127.0.0.1:5000/api/carros");
			setCarrosDisponiveis(data.carros);
			setCarrosAlugados(data.alugados);
		};
		fetchData();
	}, []);

	const alugarCarro = async (carro, dataRetirada, dataEntrega) => {
		const dataInicio = new Date(dataRetirada);
		const dataFim = new Date(dataEntrega);

		if (dataInicio >= dataFim) {
			alert("A data de retirada deve ser anterior à data de entrega!");
			return;
		}

		const diffTime = Math.abs(dataFim - dataInicio);
		const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
		const totalPreco = carro.preco * diffDays;

		const confirmacao = window.confirm(
			`Você está alugando o carro "${carro.nome}" por ${diffDays} dias. Total: R$ ${totalPreco}. Deseja continuar?`,
		);

		if (!confirmacao) {
			return;
		}

		try {
			const response = await axios.post("http://127.0.0.1:5000/api/alugar", {
				id: carro.id,
				data_retirada: dataRetirada,
				data_entrega: dataEntrega,
				dias: diffDays,
				total_preco: totalPreco,
			});
			alert(response.data.message);
			window.location.reload(); // Atualiza os dados após o aluguel
		} catch (error) {
			console.error("Erro ao alugar carro:", error);
			alert("Ocorreu um erro ao tentar alugar o carro.");
		}
	};

	const devolverCarro = async (carro) => {
		const response = await axios.post("http://127.0.0.1:5000/api/devolver", {
			id: carro.id,
		});
		alert(response.data.message);
		window.location.reload(); // Atualiza os dados após a devolução
	};

	return (
		<div className="p-4">
			<h1 className="text-3xl font-bold text-center mb-4">
				Locadora de Carros 🚗
			</h1>

			{/* Carros Disponíveis */}
			<h2 className="text-2xl font-semibold mt-6">Carros Disponíveis:</h2>
			<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
				{carrosDisponiveis.length > 0 ? (
					carrosDisponiveis.map((carro) => (
						<div key={carro.id} className="border p-4 rounded shadow">
							<h3 className="text-xl font-semibold">{carro.nome}</h3>
							<p className="text-gray-600">Preço: R$ {carro.preco} / dia</p>
							<input
								type="date"
								id={`retirada_${carro.id}`}
								className="mt-2 border p-2 rounded w-full"
							/>
							<input
								type="date"
								id={`entrega_${carro.id}`}
								className="mt-2 border p-2 rounded w-full"
							/>
							<button
								onClick={() => {
									const dataRetirada = document.getElementById(
										`retirada_${carro.id}`,
									).value;
									const dataEntrega = document.getElementById(
										`entrega_${carro.id}`,
									).value;
									if (dataRetirada && dataEntrega) {
										alugarCarro(carro, dataRetirada, dataEntrega);
									} else {
										alert("Por favor, preencha ambas as datas!");
									}
								}}
								className="mt-4 w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-700 transition duration-300"
							>
								Alugar
							</button>
						</div>
					))
				) : (
					<p>Nenhum carro disponível no momento.</p>
				)}
			</div>

			{/* Carros Alugados */}
			<h2 className="text-2xl font-semibold mt-6">Carros Alugados:</h2>
			<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
				{carrosAlugados.length > 0 ? (
					carrosAlugados.map((carro) => (
						<div key={carro.id} className="border p-4 rounded shadow">
							<h3 className="text-xl font-semibold">{carro.nome}</h3>
							<p className="text-gray-600">Preço: R$ {carro.preco} / dia</p>
							<p className="text-gray-600">Retirada: {carro.data_retirada}</p>
							<p className="text-gray-600">Entrega: {carro.data_entrega}</p>

							{/* Exibir dias e preço total após aluguel */}
							{carro.dias && carro.total_preco && (
								<div className="mt-4 text-gray-700">
									<p>
										<strong>Período de aluguel:</strong> {carro.dias} dias
									</p>
									<p>
										<strong>Total a pagar:</strong> R$ {carro.total_preco}
									</p>
								</div>
							)}

							{/* biome-ignore lint/a11y/useButtonType: <explanation> */}
							<button
								onClick={() => devolverCarro(carro)}
								className="mt-4 w-full bg-red-500 text-white py-2 rounded hover:bg-red-700 transition duration-300"
							>
								Devolver
							</button>
						</div>
					))
				) : (
					<p>Nenhum carro alugado no momento.</p>
				)}
			</div>
		</div>
	);
};

export default App;
