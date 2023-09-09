import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, FormControl } from '@angular/forms';
import { UserService } from '../../../api.service'; // Create this service to interact with the FastAPI backend

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.css']
})
export class CadastroComponent implements OnInit {
    
    ngOnInit(): void {
    }
    
    // constructor(private userService: UserService) { }
    
    onSubmit() {
        var registrationForm = new FormGroup({
            nome: new FormControl('', [Validators.required]),
            sobrenome: new FormControl('', [Validators.required]),
            telefone: new FormControl(''),
            dataNascimento: new FormControl(''),
            email: new FormControl('', [Validators.required]),
            senha: new FormControl('', [Validators.required, Validators.minLength(6)])
        });

        // this.userService.registerUser(registrationForm).subscribe(
        //     (response) => {
        //     // Handle successful registration, e.g., display a success message
        //     console.log('Registration successful', response);
        //     },
        //     (error) => {
        //     // Handle registration error, e.g., display an error message
        //     console.error('Registration error', error);
        //     }
        // );
    }
}
