import {Component, OnInit} from '@angular/core';

import { Category } from "../../../service/interfaces/category";
import {CategoriesService} from "../../../service/categories/categories.service";

@Component({
  selector: 'app-list-categories',
  templateUrl: './list-categories.component.html',
  styleUrls: ['./list-categories.component.css']
})
export class ListCategoriesComponent implements OnInit{

  categories: Category[] = [];
  constructor(private categoriesService: CategoriesService) {
    this.getCategories();
  }


  private getCategories() {
    this.categoriesService.getCategories().subscribe(
      (categories) =>
        (this.categories = categories.data))

  }

  ngOnInit(): void {
  }

  remove(id: number) {
    this.categoriesService.removeCategory(id).subscribe(
      (categories) =>
        this.categories = categories.data)
  }
}
