# How do I create a yes/no dialog box using Angular?
// plain

Creating a yes/no dialog box using Angular is a straightforward process. First, you need to import the MatDialogModule from the @angular/material package into your app.module.ts file.

```
import { MatDialogModule } from '@angular/material';

@NgModule({
  imports: [
    ...
    MatDialogModule,
  ],
  ...
})
export class AppModule { }
```

Then, you need to create a component for the dialog box. The component should include an HTML template for the dialog box and the TS file should include the code for the dialog box.

```
@Component({
  selector: 'dialog-box',
  templateUrl: 'dialog-box.html',
})
export class DialogBoxComponent {
  constructor(
    public dialogRef: MatDialogRef<DialogBoxComponent>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData
  ) {}

  onNoClick(): void {
    this.dialogRef.close();
  }
}
```

The HTML template for the dialog box should include the two buttons for the yes/no selection.

```
<h1 mat-dialog-title>Dialog Box</h1>
<div mat-dialog-content>
  <p>Do you want to continue?</p>
</div>
<div mat-dialog-actions>
  <button mat-button (click)="onNoClick()">No</button>
  <button mat-button [mat-dialog-close]="true">Yes</button>
</div>
```

Finally, you need to open the dialog box from the component where you want to use it.

```
openDialog(): void {
  const dialogRef = this.dialog.open(DialogBoxComponent, {
    width: '250px',
    data: {name: this.name, animal: this.animal}
  });

  dialogRef.afterClosed().subscribe(result => {
    console.log('The dialog was closed');
  });
}
```

The code above will create a yes/no dialog box using Angular.

## Code explanation
**

1. Importing MatDialogModule: `import { MatDialogModule } from '@angular/material';`
2. Creating DialogBoxComponent: `@Component({selector: 'dialog-box', templateUrl: 'dialog-box.html'})`
3. HTML template for the dialog box: `<h1 mat-dialog-title>Dialog Box</h1> <div mat-dialog-content> <p>Do you want to continue?</p> </div> <div mat-dialog-actions> <button mat-button (click)="onNoClick()">No</button> <button mat-button [mat-dialog-close]="true">Yes</button> </div>`
4. Opening the dialog box: `openDialog(): void { const dialogRef = this.dialog.open(DialogBoxComponent, { width: '250px', data: {name: this.name, animal: this.animal} }); dialogRef.afterClosed().subscribe(result => { console.log('The dialog was closed'); }); }`

**## Helpful links**

- [Angular Material Dialog](https://material.angular.io/components/dialog/overview)
- [Angular Material Dialog - API](https://material.angular.io/components/dialog/api)

onelinerhub: [How do I create a yes/no dialog box using Angular?](https://onelinerhub.com/angularjs/how-do-i-create-a-yes-no-dialog-box-using-angular)