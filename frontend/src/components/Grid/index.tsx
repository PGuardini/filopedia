import axios from "axios";
import { useState, useEffect } from "react";

import './grid.css'
import CardFilosofo from "../Card";

interface Filosofo {
    id: number;
    nome: string;
    biografia: string;
    imagem: string;
    slug: string;
}


const GridFilosofos = () => {

    const [filosofos, setFilosofos] = useState<Filosofo[]>([]);
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(()=>{
        const carregarDados = async (): Promise<void> => {
            try {
                const response = await axios.get<Filosofo[]>('http://localhost:8000/api/filosofos/');    
                setFilosofos(response.data);
                console.log(response.data)
            } catch (error) {
                console.log("Erro ao buscar filósofos:", error);                
            } finally {
                setLoading(false);
            }
        };

        carregarDados();
    }, []);

    if (loading) return <p>Carregando filósofos...</p>;

    return (
        <section className="philosopher-grid">
            {filosofos.map((filosofo) => (
                <CardFilosofo
                    id={filosofo.id}
                    nome={filosofo.nome}
                    biografia={filosofo.biografia}
                    imagem={filosofo.imagem}
                    slug={filosofo.slug}
                />
            ))}
        </section>
    );
};

export default GridFilosofos;