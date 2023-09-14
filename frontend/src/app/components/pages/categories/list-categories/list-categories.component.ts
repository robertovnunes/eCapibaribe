import {Component, OnInit} from '@angular/core';
import { NgIconsModule } from "@ng-icons/core";
import {Router} from "@angular/router";
import { Category } from "../../../../service/interfaces/category";
import {CategoriesService} from "../../../../service/categories/categories.service";
import { LocalStorageService } from 'src/app/service/local-storage.service';

@Component({
  selector: 'app-list-categories',
  templateUrl: './list-categories.component.html',
  styleUrls: ['./list-categories.component.css']
})
export class ListCategoriesComponent implements OnInit{

  categories: Category[] = [];
  constructor(private categoriesService: CategoriesService,private router: Router,
    private localStorageService: LocalStorageService,
    
    ) {
    this.localStorageService.set('edit_category_id', null);
    this.getCategories();
  }


  private getCategories() {
    this.categoriesService.getCategories().subscribe(
      (categories) =>
        (this.categories = categories.data))

  }

  private getCategory(category_id : number ) {
    this.categoriesService.getCategory(category_id).subscribe(
      (categories) =>
        (this.categories = categories.data))
  }

  ngOnInit(): void {
  }

  remove(id: number | null) {
    this.categoriesService.removeCategory(id!).subscribe(
      (categories) =>
        this.categories = categories.data)
  }
  
  /*edit(id: number | null) {
    this.categoriesService.editCategory(id! ).subscribe(
      (categories) =>
        this.categories = categories.data)
  }*/
  goedit(category_id : Number | null ){

    this.localStorageService.set('category_id', category_id );
    this.router.navigate(['edit-categories'], {replaceUrl: true}).then(r => r);
  }
  

  
}
