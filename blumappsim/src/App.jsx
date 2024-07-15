import { useSpring, animated } from "@react-spring/web";
import "./main.css";
import { useState } from "react";

export const CUBE_SIZE = window.innerWidth / 10

const Cube = (propss) => {
  const props = useSpring({
    loop: true,
    from: { transform: "translateY(0px)" },
    to: { transform: `translateY(${window.innerHeight})` },
    config: { duration: 2500 },
  });
  let [opacity, setOpacity] = useState(1)
  return (
    <div
    onClick={() => {
          
          setOpacity(0)
          console.log("aa " + opacity);
        }}
      style={{
        margin: propss.margin,
        opacity: opacity,
      }}
    >
      <animated.div
        className="cube"
        style={props}
        
      ></animated.div>
    </div>
  );
};

const CubeBulk = () => {
  const cubeCount =  Math.floor(Math.random() * 4) + 1
  const leftWidth = window.innerWidth - (CUBE_SIZE * 2)
  const fixedMargin = leftWidth * (3/4) / cubeCount
  const preservedMargin = leftWidth * (1/4)

  let cubelist = [];
  for (let i = 0; i < cubeCount; i++) {
    cubelist.push(<Cube margin={`${fixedMargin}px`} key={i} />);
  }
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "row",
      }}
    >
      {cubelist}
    </div>
  );
};

const App = () => {
  return (
    <>
      <CubeBulk />
    </>
  );
};

export {App};
