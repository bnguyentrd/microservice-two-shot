# Wardrobify

Team:

* Bobby - Hats
* Anthony - Shoes

## Design
Webpage > shop > categories > sizes




## Shoes microservice

Experiments/Concerns:
    - In poller.py forgot to call get_bin function in poller function. This caused a lot of back and forth concerning a 400 error on insomnia.
        -
    - Unique key was cauing a problem with React fetching. The developer console was showing data, but React did not enjoy that I did not use a unqiue key specific to each object.

Differences in our form class:
ShoesForm.js > class ShoesForm constructor >in this.state i have bin: "" and bins: []
explanation: empty array for the drop down bar and the empty string to show that single piece of information.



Anthony's explanations


Explain your models and integration with the wardrobe
microservice, here.

## Hats microservice
Bobby's explanations

HatsForm.js, line 44: Added empty string for location variable(test)
explanation: Since we have an empty array, i made an empty string inside handleSubmit to catch each value inside the array(which would be created by user)

input tag: declaring value={this.state...}(test)
explanation: A value for the user input




Explain your models and integration with the wardrobe
microservice, here.
