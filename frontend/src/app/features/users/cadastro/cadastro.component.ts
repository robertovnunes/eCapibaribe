import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, FormControl} from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { User } from '../users/user';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.css']
})
export class CadastroComponent implements OnInit {
    user: User;
    constructor(private http: HttpClient) { }
    
    ngOnInit(): void {
        this.user = new User();
        console.debug("entrei init")
    }
    
    
    onSubmit() {
        console.log(this.user);
        
        this.http.post("http://localhost:8000/users/register", {"nome": this.user.nome, "sobrenome": this.user.sobrenome, "cpf": this.user.cpf, "telefone": this.user.telefone, "senha": this.user.senha, "email": this.user.email, "dataNascimento": this.user.dataNascimento})
        // ao instanciar novamente o objeto cliente, você vai limpar os controles na tela
        this.user = new User();
      }
}
