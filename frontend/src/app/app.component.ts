import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'ecommerce';
  categorias = [
    {nome: 'Eletrônicos', descricao: 'Eletrônicos em geral', imagem: 'https://picsum.photos/200/300'},
    {nome: 'Eletrodomésticos', descricao: 'Eletrodomésticos em geral', imagem: 'https://picsum.photos/200/300'},
    {nome: 'Móveis', descricao: 'Móveis em geral', imagem: 'https://picsum.photos/200/300'},
    {nome: 'Roupas', descricao: 'Roupas em geral', imagem: 'https://picsum.photos/200/300'},
    {nome: 'Calçados', descricao: 'Calçados em geral', imagem: 'https://picsum.photos/200/300'},
    {nome: 'Acessórios', descricao: 'Acessórios em geral', imagem: 'https://picsum.photos/200/300'}
  ]
  itens!: {nome: string, descricao: string, imagem: string}[];
}
