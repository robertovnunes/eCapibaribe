import {
    HttpEvent,
    HttpHandler,
    HttpInterceptor,
    HttpRequest,
} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable, map } from 'rxjs';
import { environment } from 'src/environments/environments.dev';

@Injectable()
export class HttpRequestInterceptor implements HttpInterceptor {
    apiUrl: string = environment.apiUrl;

    intercept(
        req: HttpRequest<any>,
        next: HttpHandler
    ): Observable<HttpEvent<any>> {
        req = req.clone({
            url: `${this.apiUrl}${req.url}`,
        });
        return this.handler(req, next);
    }

    handler(req: HttpRequest<any>, next: HttpHandler) {
        return next
            .handle(req)
            .pipe(
                catchError(error => {
                    return error;
                })
            )
            .pipe(
                map<HttpEvent<any> | unknown, any>(event => {
                    return event;
                })
            );
    }
}
