import { useState, useEffect } from "react";
import axios from "axios"; //Biblioteca para realizar requisições HTTP, facilita chamadas GET/POST, lidando automaticamente com headers e payloads.
//useState e useEffect: Hooks do React usados para gerenciamento de estado e efeitos colaterais.
//Por quê? useState armazena o estado da aplicação (carros disponíveis e alugados). useEffect faz a chamada inicial para a API ao carregar a página.

//Estados iniciais
const App = () => {
	const [carrosDisponiveis, setCarrosDisponiveis] = useState([]); //Função: Gerenciar os carros disponíveis e alugados. Inicialmente, ambos são arrays vazios.
	const [carrosAlugados, setCarrosAlugados] = useState([]); //Os dados são preenchidos ao carregar a página com os valores retornados pela API.

	// Carregando dados com useEffect
	useEffect(() => {
		const fetchData = async () => {
			const { data } = await axios.get("http://127.0.0.1:5000/api/carros"); //Faz uma chamada HTTP para buscar os carros do backend e atualiza os estados.
			setCarrosDisponiveis(data.carros); //Garante que os dados exibidos na interface sejam atualizados diretamente da API.
			setCarrosAlugados(data.alugados);
		};
		fetchData();
	}, []);

	// Função de alugar um carro
	const alugarCarro = async (carro, dataRetirada, dataEntrega) => {
		const dataInicio = new Date(dataRetirada);
		const dataFim = new Date(dataEntrega);

		if (dataInicio >= dataFim) {
			alert("The pick-up date must be before the delivery date!");
			return;
		}

		const diffTime = Math.abs(dataFim - dataInicio); //A função Math.abs() é usada para garantir que a diferença seja positiva, ou seja, não importa qual data é maior, a diferença será sempre um valor positivo.
		const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); //diffTime = 9 dias * 24 horas/dia * 60 minutos/hora * 60 segundos/minuto * 1000 milissegundos/segundo
		//O Math.ceil() é usado para arredondar para cima, ou seja, se a diferença for, por exemplo, 5,2 dias, o valor será arredondado para 6.
		const totalPreco = carro.preco * diffDays; //diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)) = 9 = > totalPreco = 100 * 9 = 900

		const confirmacao = window.confirm(
			`You're renting the car"${carro.nome}" for ${diffDays} days. Totals: R$ ${totalPreco}. Do you want to continue? 👍`,
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
			console.error("Car rental mistakes:", error);
			alert("An error occurred while trying to rent a car.");
		}
	};

	// Função de devolver um carro
	const devolverCarro = async (carro) => {
		//funcao, faz a requisição para devolver o carro
		const response = await axios.post("http://127.0.0.1:5000/api/devolver", {
			id: carro.id,
		});
		alert(response.data.message);
		window.location.reload(); // Atualiza os dados após a devolução
	}; //Atualiza o backend e recarrega os dados para refletir as mudanças.

	//  Renderização com Tailwind CSS
	return (
		<div className="p-4">
			<h1 className="text-3xl font-bold text-center mb-4">Car Rental 🚗🚓🚙</h1>

			{/* Carros disponíveis: mapeia e renderiza */}
			<h2 className="text-2xl font-semibold mt-6">Available Cars 🚓🧐:</h2>
			<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
				{carrosDisponiveis.length > 0 ? (
					carrosDisponiveis.map(
						(
							carro, //Usa map para iterar sobre os arrays e renderizar componentes dinamicamente.
						) => (
							<div key={carro.id} className="border p-4 rounded shadow">
								<h3 className="text-xl font-semibold">{carro.nome}</h3>
								<p className="text-gray-600">Price: R$ {carro.preco} / day</p>
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
									type="button" // Define explicitamente o tipo do botão
									onClick={() => {
										const dataRetirada = document.getElementById(
											`retirada_${carro.id}`,
										)?.value; // Use o operador de encadeamento opcional para evitar erros caso o elemento não exista
										const dataEntrega = document.getElementById(
											`entrega_${carro.id}`,
										)?.value; // Use o operador de encadeamento opcional para evitar erros caso o elemento não exista
										if (dataRetirada && dataEntrega) {
											alugarCarro(carro, dataRetirada, dataEntrega);
										} else {
											alert("Please enter both dates!");
										}
									}}
									className="mt-4 w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-700 transition duration-300"
								>
									Rent
								</button>
							</div>
						),
					)
				) : (
					<p>No cars available at the moment😥.</p>
				)}
			</div>

			{/* Carros alugados: mapeia e renderiza */}
			<h2 className="text-2xl font-semibold mt-6">Rental Cars:</h2>
			<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
				{carrosAlugados.length > 0 ? (
					carrosAlugados.map((carro) => (
						<div key={carro.id} className="border p-4 rounded shadow">
							<h3 className="text-xl font-semibold">{carro.nome}</h3>
							<p className="text-gray-600">Rent: R$ {carro.preco} / day</p>
							<p className="text-gray-600">Pick up: {carro.data_retirada}</p>
							<p className="text-gray-600">Delivery: {carro.data_entrega}</p>

							{/* Exibir dias e preço total após aluguel */}
							{carro.dias && carro.total_preco && (
								<div className="mt-4 text-gray-700">
									<p>
										<strong>Rental period:</strong> {carro.dias} days
									</p>
									<p>
										<strong>Total pay:</strong> R$ {carro.total_preco}
									</p>
								</div>
							)}

							{/* biome-ignore lint/a11y/useButtonType: <explanation> */}
							<button
								onClick={() => devolverCarro(carro)}
								className="mt-4 w-full bg-red-500 text-white py-2 rounded hover:bg-red-700 transition duration-300"
							>
								Return
							</button>
						</div>
					))
				) : (
					<p>No car rented at the moment 😉</p>
				)}
			</div>
		</div>
	);
};

export default App;
