import './card.css'

interface Filosofo {
    id: number;
    nome: string;
    biografia: string;
    imagem: string;
    slug: string;
}

const CardFilosofo = ({ id, nome, biografia, imagem, slug}: Filosofo) => {
    return (
        <article className="card">
            <div className="card-image">
                <img src={`https:${imagem}`} alt={`Retrato de ${nome}`} />
            </div>

            <div className="card-content">
                <h2 className="name">{nome}</h2>
                <p className="">{biografia.substring(0, 250)}</p>
                <p className="meta">
                    <a href={`/${slug}`}>Ler mais</a>
                </p>
            </div>
        </article>
    );
}

export default CardFilosofo;