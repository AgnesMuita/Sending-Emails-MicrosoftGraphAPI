import React,{useState} from "react";


function Form() {
    const[showPage, showSetPage] = useState(false);

    const handlePreviousPage=()=>{
        showSetPage(true)
    }
    const handleNextPage=()=>{
        showSetPage(false)
    }
    return (
      <div className="row">
      <div className="col-md-6 col-md-offset-3">
          <form id="msform">
              <ul id="progressbar">
                  <li className="active">Configurations</li>
                  <li>Compose Email</li>
              </ul>
              {showPage ?
                <fieldset>
                  <h2 className="fs-title">Configurations</h2>
                  <input type="text" name="ClientId" placeholder="Client Id"/>
                  <input type="text" name="tenantId" placeholder="Tenant Id"/>
                  <input type="text" name="sendersemail" placeholder="Senders Email"/>
                  <input type="password" name="password" placeholder="Password"/>
                  <input type="button" name="next" className="next action-button" value="Next" onClick={handleNextPage}/>
              </fieldset>
              :
              <fieldset>
                  <h2 className="fs-title">Compose Email</h2>
                  <h3 className="fs-subtitle">Compose Email</h3>
                  <input type="text" name="recipient" placeholder="To"/>
                  <input type="text" name="subject" placeholder="subject"/>
                  <input type="text" name="message" placeholder="message"/>
                  <input type="button" name="previous" className="previous action-button-previous" value="Previous" onClick={()=>handlePreviousPage()}/>
                  <input type="submit" name="submit" className="submit action-button" value="Submit"/>
              </fieldset>
              }
          </form>
          <div className="dme_link">
              <p><a href="https://agnes-muita.vercel.app/" target="_blank" rel='noreferrer'>Design By Aggie</a></p>
          </div>
        </div>
        </div>
    )

}

export default Form