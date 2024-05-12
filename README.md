# Projeto de Contação de Histórias para Crianças

Este projeto tem como objetivo incentivar a contação de histórias "por crianças para crianças", permitindo que elas gravem vídeos de suas próprias histórias, que serão aprimoradas e publicadas. Além disso, o projeto inclui a recomendação de livros (dentro de um universo curto, de experimentação) e a comparação entre a história autoral e obras recomendadas, visando estimular a criatividade e promover o gosto pela leitura e criação.

Link para execução direto do google colab: https://drive.google.com/file/d/1BLhdmbv6p28D6rb18-EIMMj0YakLxMS7/view?usp=sharing
## Como Subir um vídeo: 
Link como fazer uma execução com o vídeo: https://github.com/Evandro15/Alura_Kid_4_kids/blob/c5caa805b80a9bfa88a3bd86a77ea5743f3c79fa/Demonstra%C3%A7%C3%A3o%20de%20Importa%C3%A7%C3%A3o%20do%20V%C3%ADdeo.mp4

## Tecnologias Utilizadas
- Google Generative AI (Gemini)
- Web Scraping
- Transformação de Vídeo em Texto
- Embeddings
- Técnicas LLM: Chain of Thought, Few Shot

## Utilização
Neste primeiro momento, o projeto deve ser executado através do Google Colab ou plataforma similar. Em versões futuras, será implementada uma API para permitir o upload do arquivo e a geração por meio de um site na plataforma Heroku.

### Passo a Passo
1. O script realizará um scraping da plataforma [Toda Matéria - Literatura](https://www.todamateria.com.br/literatura/resumos-de-livros/) para obter resenhas de livros.
2. Em seguida, transcreverá o vídeo gravado para texto e fará a leitura do mesmo para extrair a história.
3. Utilizando o modelo Gemini da Google, gerará uma resenha sobre a história contada e a enriquecerá de forma simples.
4. Fará embeddings dos livros na LLM para criar sugestões dos livros que mais se aproximam da história contada.
5. Entregará um resumo da obra recomendada e gerará um paralelo entre a história autoral e a recomendada, para que a criança entenda as semelhanças.

## Demo
Link para um vídeo de uma criança contando história: https://drive.google.com/file/d/1hBzLiEbNGiBY5rP56hf2jZOFiHe-dRZM/view?usp=drive_link
Link para o resultado do processamento: https://github.com/Evandro15/Alura_Kid_4_kids/blob/3342d4791d6362303f1035c39470134c0c4ca9ad/ReviewLer_2024-05-11_22-15-25.html

### Próximos Passos
- Implementar uma API para permitir o upload do arquivo e a geração por meio do site na plataforma Heroku.
- Adicionar novas funcionalidades, como citar o nome do autor e capturar características da pessoa do vídeo utilizando o modelo Gemini.
- Oferecer suporte para escolha de geração com base em estilos predefinidos, como romance, gótico, cordel, poesia, entre outros.

Este projeto foi desenvolvido com o modelo Gemini da Google e destina-se ao uso educacional, principalmente para a plataforma Alura. No repositório, estará disponível um vídeo de exemplo e um documento com o resultado do processamento.

Fique à vontade para contribuir e sugerir melhorias!
