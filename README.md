# Projeto de Contação de Histórias para Crianças

Este projeto tem como objetivo incentivar a contação de histórias para crianças, permitindo que elas gravem vídeos de suas próprias histórias, que serão aprimoradas e publicadas. Além disso, o projeto inclui a recomendação de livros e a comparação entre a história autoral e obras recomendadas, visando estimular a criatividade e promover o gosto pela leitura.

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

### Próximos Passos
- Implementar uma API para permitir o upload do arquivo e a geração por meio do site na plataforma Heroku.
- Adicionar novas funcionalidades, como citar o nome do autor e capturar características da pessoa do vídeo utilizando o modelo Gemini.
- Oferecer suporte para escolha de geração com base em estilos predefinidos, como romance, gótico, cordel, poesia, entre outros.

Este projeto foi desenvolvido com o modelo Gemini da Google e destina-se ao uso educacional, principalmente para a plataforma Alura. No repositório, estará disponível um vídeo de exemplo e um documento com o resultado do processamento.

Fique à vontade para contribuir e sugerir melhorias!
