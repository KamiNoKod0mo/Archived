-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 03-Out-2023 às 20:37
-- Versão do servidor: 10.4.24-MariaDB
-- versão do PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `rede_social_curso_devweb20`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `amizades`
--

CREATE TABLE `amizades` (
  `id` int(11) NOT NULL,
  `enviou` int(11) NOT NULL,
  `recebeu` int(11) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `amizades`
--

INSERT INTO `amizades` (`id`, `enviou`, `recebeu`, `status`) VALUES
(4, 1, 5, 1),
(5, 5, 3, 1),
(6, 1, 4, 1),
(9, 1, 3, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `clientes`
--

CREATE TABLE `clientes` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `sobrenome` varchar(255) NOT NULL,
  `momento_registro` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `clientes`
--

INSERT INTO `clientes` (`id`, `nome`, `sobrenome`, `momento_registro`) VALUES
(1, 'sdfasdf', 'asdfasd', '2023-07-18 15:41:11');

-- --------------------------------------------------------

--
-- Estrutura da tabela `posts`
--

CREATE TABLE `posts` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `post` text NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `posts`
--

INSERT INTO `posts` (`id`, `usuario_id`, `post`, `date`) VALUES
(1, 1, 'Meu texto', '2021-04-05 20:53:54'),
(2, 1, 'olá', '2021-04-05 15:55:20'),
(3, 1, 'Olá mundo', '2021-04-05 16:00:23'),
(4, 1, 'Oi! Meu post para meus amigos!', '2021-04-05 16:02:55'),
(5, 1, '\r\nOlá mundo\r\n\r\n', '2021-04-07 15:13:26'),
(6, 1, '\r\nPessoal, olha esse curso que da hora! [imagem=https://cursos.dankicode.com/app/Views/public/images/uploads/cursos/591f197b0f718.jpg]\r\n\r\n', '2021-04-07 15:13:56'),
(7, 1, '\r\nOpa!\r\n\r\n', '2021-04-07 15:15:01'),
(8, 1, '\r\nOpa olha que bacana! [imagem=https://cursos.dankicode.com/app/Views/public/images/uploads/cursos/591f197b0f718.jpg]\r\n\r\n', '2021-04-07 15:15:23'),
(9, 1, '\r\nOpa olha que bacana!\r\n\r\n', '2021-04-07 15:16:06'),
(10, 3, '\r\nAh... To com sono\r\n\r\n', '2021-04-12 15:41:16'),
(11, 5, '\r\nlol! Olha isso cara\r\n\r\n', '2021-04-12 15:41:39'),
(12, 1, '\r\nOlá, aqui eh um post meu próprio!\r\n\r\n', '2021-04-12 16:04:22'),
(13, 4, '\r\nOi! Aqui é o joaozinho1.\r\n\r\n', '2021-04-12 16:32:40'),
(14, 1, '\r\nok\r\n\r\n', '2021-04-12 16:40:24'),
(15, 4, '\r\nOpa! Novo post e é pra sumir do gui.\r\n\r\n', '2021-04-12 16:42:39'),
(16, 1, '\r\nOi\r\n\r\n', '2021-04-14 22:10:34'),
(17, 4, '\r\nOpa!\r\n\r\n', '2021-04-19 12:51:52');

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `senha` text NOT NULL,
  `ultimo_post` datetime ,
  `img` text ,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `nome`, `email`, `senha`, `ultimo_post`, `img`) VALUES
(1, 'Guilherme Grillo', 'guilhermegrillo.13@gmail.com', '$2a$08$MTQwNDExODAxOTYwN2RhNOR5/AqYak4c6KSVIlkxE9Xfrr7QWRdq2', '2021-04-14 22:10:34', '607da5ad82b62.jpg'),
(2, 'William', 'gui_grillo13@hotmail.com', '$2a$08$NDIyMDExNDc5NjA0Nzk3OOwXZD/cxhWlx1AUQREZroTYBEvgNmZm2', '0000-00-00 00:00:00', ''),
(3, 'Joao Ferreira', 'joaozinho@hotmail.com', '$2a$08$NDIyMDExNDc5NjA0Nzk3OOwXZD/cxhWlx1AUQREZroTYBEvgNmZm2', '2021-04-12 15:41:16', ''),
(4, 'Pedro', 'joaozinho1@gmail.com', '$2a$08$NDIyMDExNDc5NjA0Nzk3OOwXZD/cxhWlx1AUQREZroTYBEvgNmZm2', '2021-04-19 12:51:52', '607da75aa16bb.jpg'),
(5, 'Joao Lucas', 'joaozinho2@gmail.com', '$2a$08$NDIyMDExNDc5NjA0Nzk3OOwXZD/cxhWlx1AUQREZroTYBEvgNmZm2', '2021-04-12 15:41:39', '');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `amizades`
--
ALTER TABLE `amizades`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`);



--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `amizades`
--
ALTER TABLE `amizades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de tabela `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `posts`
--
ALTER TABLE `posts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
