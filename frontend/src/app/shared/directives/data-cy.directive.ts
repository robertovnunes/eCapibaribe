import { Directive, ElementRef, Input } from '@angular/core';

@Directive({
    selector: '[dataCy]',
})
export class DataCyDirective {
    @Input() set dataCy(value: string) {
        this.elementRef.nativeElement.setAttribute('dataCy', value);
    }

    constructor(private elementRef: ElementRef) {}
}
