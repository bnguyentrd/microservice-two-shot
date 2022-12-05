# Wardrobify

Team:

* Bobby - Hats
* Anthony - Shoes

## Design
Webpage > shop > categories > sizes




## Shoes microservice

ShoesForm.js > class ShoesForm constructor >in this.state i have bin: "" and bins: []
explanation: empty array for the drop down bar and the empty string to show that single piece of information.

Anthony's explanations


Explain your models and integration with the wardrobe
microservice, here.

## Hats microservice
Bobby's explanations

Experiments/Concerns:

HatsForm.js, line 44: Added empty string for location variable(test)
explanation: Since we have an empty array, i made an empty string inside handleSubmit to catch each value inside the array(which would be created by user)

input tag: declaring value={this.state...}(test)
explanation: A value for the user input

In poller.py, we forgot to input get_locations function inside poll function which was causing 400 errors on insomnia




Step by Step:
1. We registered the hats app inside hats_project's settings.py, under INSTALLED_APPS.
2. We created models inside hats api models.py(LocationVO and Hats)
3. We created view functions to show the list of our models.(LocationVODetailEncoder, HatListEncoder, HatDetailEncoder)
4. 




Explain your models and integration with the wardrobe
microservice, here.
