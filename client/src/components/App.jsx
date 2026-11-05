import { Route, Routes } from "react-router";
import Home from "./Home";
import Navbar from "./NavBar";
import Restaurant from "./Restaurant";

function App() {

  const API_URL="http://0.0.0.0:8080"
  return (
    <>
      <Navbar />
      <Routes>
        <Route
          path="/restaurants/:id"
          element={<Restaurant API_URL={API_URL}/>}
        />
        <Route 
         path="/"
          element={<Home API_URL={API_URL}/>}
        />
      </Routes>
    </>
  );
}

export default App;