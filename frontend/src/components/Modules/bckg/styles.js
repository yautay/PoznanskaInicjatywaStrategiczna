import styled from 'styled-components'

export const background = styled.div`
  &, &::before, &::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  &::before {
    content: "";
    position: absolute;
    height: 100%;
    width: 100%;
    background-image: url("https://video-images.vice.com/articles/6115489f19c3ad0093db714c/lede/1628785413703-screen-shot-2021-08-12-at-122251-pm.png?crop=1xw:0.6631xh;0xw,0xh&resize=500:*");
    background-position: center;
    background-size: cover;
    background-attachment: fixed;
    filter: grayscale(80%) brightness(180%) contrast(105%);
    z-index: -10;
  }
`;

export const background__shadow = styled.div`
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.15);
  z-index: -2;
  @media (min-width: 768px) {
    body .bg::before {
      background-image: url("../img/wood-1200.jpg");
    }
  }
  @media (min-width: 1200px) {
    body .bg::before {
      background-image: url("../img/wood-3000.jpg");
    }
  }
`;

export default background;
