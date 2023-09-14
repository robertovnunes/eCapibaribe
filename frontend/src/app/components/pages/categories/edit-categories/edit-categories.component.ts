import {Component, Input, OnInit} from '@angular/core';
import { Category } from "../../../../service/interfaces/category";
import {FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";
import {Router} from "@angular/router";
import {CategoriesService} from "../../../../service/categories/categories.service";
import { LocalStorageService } from 'src/app/service/local-storage.service';

@Component({
  selector: 'app-edit-categories',
  templateUrl: './edit-categories.component.html',
  styleUrls: ['./edit-categories.component.css']
})
export class EditCategoriesComponent implements OnInit {
  
  nameInput!: HTMLInputElement | null;
  descInput!: HTMLInputElement | null;
  keywordsInput!: HTMLInputElement | null;
  imageInput!: HTMLInputElement | null;

  name: FormControl<string | null>
  desc: FormControl<string | null>
  keywords: FormControl<string | null>
  image: FormControl<string | null>

  form: FormGroup;



  constructor(private readonly fb: FormBuilder,
              private localStorageService: LocalStorageService,
              private router: Router,
              private categoriesService: CategoriesService) {
              this.name = this.fb.control('', [Validators.required]);
              this.desc = this.fb.control('', [Validators.required]);
              this.keywords = this.fb.control('', [Validators.required]);
              this.image = this.fb.control('', [Validators.required]);
              this.form = this.fb.nonNullable.group({
              name: this.name,
              desc: this.desc,
              keywords: this.keywords,
              image: this.image
    });
  }

  ngOnInit(): void {
    this.nameInput = document.querySelector('input[name="name"]');
    this.descInput = document.querySelector('input[name="desc"]');
    this.keywordsInput = document.querySelector('input[name="keywords"]');
    this.imageInput = document.querySelector('input[name="image"]');
  }


  cancelar(){
    this.router.navigate(['list-categories'], {replaceUrl: true}).then();
  }

  salvar(category_id: number){
    let result;
    let message;
    let newCategory: Category;
    newCategory = {} as Category;
    if (!(this.name == null || this.desc == null || this.keywords == null || this.image == null)) {
      newCategory.name = <string>this.name.value;
      newCategory.description = <string>this.desc.value;
      newCategory.keywords = [<string>this.keywords.value];
      newCategory.image = <string>this.image.value;
      newCategory.items = [];
      console.log("**********************************");
      console.log(this.localStorageService.get('category_id'));

      category_id =this.localStorageService.get('category_id');
      this.categoriesService.editCategory(category_id, newCategory).subscribe(res => {
        result = res.status_code;
        message = res.message;
      });


      alert("Categoria atualizada com sucesso!");
      this.router.navigate(['list-categories'], {replaceUrl: true}).then(r => r);
    }
    return true;
  }


}
