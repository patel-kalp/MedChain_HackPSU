let getRequirements = () => {
    document.getElementById('text').style.visibility = "visible";
    let numOfPeople = document.getElementById("numberofPeople").value;
    // 40 patients per doctor
    let numOfDoctors = Math.round(parseInt(numOfPeople) / 40);
    // 60 patients per doctor
    let numOfNurses = Math.round(parseInt(numOfPeople) / 60);
    // Each patient there for 14 days
    // 1 PPE per day (1 for doctor and 1 per nurse)
    // Prediction for 30 days, so multiply by 2
    let numOfPPE = (numOfDoctors + numOfNurses) * 30;
    document.getElementById('PPE_Prediction').innerHTML = `Based on the predicted cases for the next 30 days. We recommended having ${numOfPPE} PPE units before on Nov 3rd. 2020.`
    document.getElementById('doctorsNursesPrediction').innerHTML = `It is advised to have ${numOfDoctors} ER doctors and ${numOfNurses} nurses on the field during the week of Nov 3rd. 2020.`;
}

function countyPA(){
    var selected = document.getElementById("midTitle").value;
    var i;
    // for loop to print data based on scroll down
    for (i=0;i<68;i++){
        if (selected==i){
            print()
        }else{
            i++;
        }
    }
}